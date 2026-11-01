from .BaseDataModel import BaseDataModel
from .db_schemes import Asset
from .enums.DataBaseEnum import DataBaseEnum
from .db_schemes import Project
from bson import ObjectId


class AssetModel(BaseDataModel):
    def __init__(self, db_clint: object):
        super().__init__(db_clint=db_clint)
        self.collection = self.db_clint[DataBaseEnum.COLLECTION_ASSET_NAME.value]

    @classmethod
    async def create_instance(cls, db_clint: object):
        instance = cls(db_clint)
        await instance.init_collection()
        return instance


    async def init_collection(self):
        all_collections = await self.db_clint.list_collection_names()
        if DataBaseEnum.COLLECTION_ASSET_NAME.value not in all_collections:
            self.collection = self.db_clint[DataBaseEnum.COLLECTION_ASSET_NAME.value]
            indexes = Asset.get_indexes()
            for index in indexes:
                await self.collection.create_index(
                    index["key"],
                    name=index["name"],
                    unique=index["unique"]
                )

    async def create_asset(self, asset: Asset):
        result = await self.collection.insert_one(asset.dict(by_alias=True, exclude_unset=True))
        asset.id = result.inserted_id

        return asset

    async def get_all_project_assets(self, asset_project_id: str):
        return await self.collection.find({
            "asset_project_id": ObjectId(asset_project_id) if isinstance(asset_project_id, str) else asset_project_id
        }).to_list(length=None)



