 Login::Login(QWidget *parent)
     : QMainWindow(parent),
       ui(new Ui::Login),
      gifTimer(new QTimer(this)),
      currentGifIndex(0),
       gifPaths({
           "/home/zouari_omar/Documents/Daily/Projects/Astra/project/assets/login imgs/animations/an00.gif",
           "/home/zouari_omar/Documents/Daily/Projects/Astra/project/assets/login imgs/animations/an01.gif",
           "/home/zouari_omar/Documents/Daily/Projects/Astra/project/assets/login imgs/animations/an02.gif",
           "/home/zouari_omar/Documents/Daily/Projects/Astra/project/assets/login imgs/animations/an03.gif",
           "/home/zouari_omar/Documents/Daily/Projects/Astra/project/assets/login imgs/animations/an04.gif",
       }),
       currentMovie(nullptr),
       generated_password("") {
   ui->setupUi(this);
   sl = nullptr;
 
   if (res.empty())
    qDebug() << "User not found";
   else
     emit loginSuccessful();
 }
 
   (void)QtConcurrent::run([this, _email, employee, progressDialog]() {
     try {
      generated_password = Password::generate(5);
       EmailSender email{EmailAuth{}};
       email.send(EmailData(
           _email,