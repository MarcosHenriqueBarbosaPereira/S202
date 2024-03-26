from database import Database
from writeAJson import writeAJson
from pokedex import Pokedex

dex = Pokedex(Database(database="pokedex", collection="pokemons"))
#db.resetDatabase()

writeAJson(dex.getSecondStagePokemonByType(["Fire", "Water"]), "SecondStageFireWater")

writeAJson(dex.getDualTypeFinalStageByType(["Fire", "Water"]), "DualTypeFinalStageFireWater")

writeAJson(dex.getEvolutionChain("Charmander"), "CharmanderEvolutionChain")

writeAJson(dex.getSingleStagePokemonFromEggDistance("10 km"), "SingleStage10kmEgg")

writeAJson(dex.getSingleTypePokemonByWeaknesses(["Fire"]), "SingleTypeFireWeaknesses")
