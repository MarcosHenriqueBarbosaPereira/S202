from database import Database
import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def getSecondStagePokemonByType(self, types: list):
        return self.database.collection.find({ "type": {"$in": types}, "next_evolution": {"$exists": True}, "prev_evolution": {"$exists": True} })
    
    def getDualTypeFinalStageByType(self, types: list):
        return self.database.collection.find({ "type": {"$in": types, "$size": 2}, "next_evolution": {"$exists": False} })

    def getEvolutionChain(self, name: str):
        return self.database.collection.find({ "$or": [{"name": name}, {"prev_evolution.name": name}, {"next_evolution.name": name}] })
    
    def getSingleStagePokemonFromEggDistance(self, distance: str):
        return self.database.collection.find({ "egg": distance, "next_evolution": {"$exists": False}, "prev_evolution": {"$exists": False} })
    
    def getSingleTypePokemonByWeaknesses(self, types: list):
        return self.database.collection.find({ "weaknesses": {"$in": types}, "type": {"$size": 1} })
    


    