def clicked(self,txt):
    self.DisplayLabel.setText( txt)
    self.DisplayLabel.adjustSize()



self.actionSave.triggered.connect(lambda:self.clicked("Paste Option"))
self.actionSave_2.triggered.connect(lambda:self.clicked("Save button under file"))
self.actionEdit.triggered.connect(lambda:self.clicked("Edit Button under file"))
self.actionNew.triggered.connect(lambda:self.clicked("Copy Option"))




#Images DEMO

#Inserted Content
def changePhoto(self,dirx):
    self.photoIndex+=dirx
    if self.photoIndex >= len(self.photoPaths):
        self.photoIndex=0
    elif self.photoIndex <0:
        self.photoIndex= len(self.photoPaths)-1
    self.Photo.setPixmap(QtGui.QPixmap(self.photoPaths[self.photoIndex])) 
#Inserted Content 

#Inserted Content
self.photoPaths=["C:/Users/DELL/Pictures/5X9Zpmw.jpg","C:/Users/DELL/Pictures/0Xun9D3.jpg"]
self.photoIndex=0
#Inserted Content