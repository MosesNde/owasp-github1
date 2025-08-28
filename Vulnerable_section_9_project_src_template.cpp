   GifButton(PDF_gif, "../global/PDF.gif", ui->PDF);
   GifButton(Notif_gif, "../global/Notif.gif", ui->Notification);
   GifButton(Wen_gif, "../global/Wen.gif", ui->Wen);

  // Init Icons
  IconButton(ui->Add_button, "../   global/Add.png", 25, 25);
  IconButton(ui->Boutiques_B, "../global/Boutiques.png", 40, 40);
  IconButton(ui->Commercants_B, "../global/Commercants.png", 40, 40);
  IconButton(ui->Partenariats_B, "../global/Partenariats.png", 40, 40);
  IconButton(ui->Evenements_B, "../global/Evenements.png", 40, 40);
  IconButton(ui->Personnels_B, "../global/Personnels.png", 40, 40);
  IconButton(ui->Employe_B, "../global/Employes.png", 40, 40);
  IconButton(ui->Cancel_form, "../global/Close.png", 20, 20);
 }
 
 // Init Widget Shadows
void ModelUi::InitShadows() {
   ui->Background_navigation->setGraphicsEffect(Shadow_Effect[0]);
   ui->Search_bar->setGraphicsEffect(Shadow_Effect[1]);
   ui->Add_button->setGraphicsEffect(Shadow_Effect[2]);
 // Init all images
 void ModelUi::InitImages() {
   // Init label images
  ScaleImage("../global/Person.jpg", ui->User_Image, 35, 35);
  ui->Logo->setPixmap(QPixmap("../global/Logo.png").scaled(ui->Logo->size()));
 
   // Init button images
   InitImageButtons();