import app
import readerJson

if __name__ == "__main__":
    readJson = readerJson.ReadorJSON('/src/plantsFile.json')
    readJson.readFromJson()
    appInst = app.App(readJson.getPlantsJson())
    appInst.mainloop()
