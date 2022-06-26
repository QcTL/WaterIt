import app
import readerJson

if __name__ == "__main__":
    readJson = readerJson.ReadorJSON('/src/plantsFile.json')
    appInst = app.App(readJson.getPlantsJson())
    appInst.mainloop()
