import logo from './logo.svg';
import './App.css';

function App() {
 
 App.use(express.json())
 App.use(express.urlencoded({extended: false}))
 App.use(cookieParser())
 App.use(express.static(Path2D.join(__dirname, "public")))
 
 const io = require("socket.io")();
 io.listen(9999);
 io.sockets.on("connection", (socket) => {
  socket.on("test", (msg) => {
    console.log(msg);
  })
 })

 App.use("/", indexRouter)
 App.use("/users", usersRouter)

 App.use(function (req, res, next) {
  next(createError(404))
 })

  return (





  );
}

export default App;
