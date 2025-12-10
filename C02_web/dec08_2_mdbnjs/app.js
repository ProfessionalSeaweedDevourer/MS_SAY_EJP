var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// node.js: js로 백엔드 구동
// mongodb: js로 db 제어
// mongojs 활용

app.listen(8888);

app.get("/snack.reg", function (req, res) {

  // var mjs = require("mongojs");

  // // "서버/db", ["테이블", "테이블", ...]
  // var db = mjs("195.168.9.225/dec08", ["dec08_snack"])
  // 한 줄로 처리
  var db = require("mongojs")("195.168.9.225/dec08", ["dec08_snack"]);

  var name = req.query.n;
  var price = req.query.p * 1;
  var snack = {"s_name": name, "s_price": price};

  db.dec08_snack.insertOne(snack, function(errr, resulttt){
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.send(resulttt);
  });

});

app.get("/snack.get", function (req, res){
  var db = require("mongojs")("195.168.9.225/dec08", ["dec08_snack"]);

  db.dec08_snack.find(function() {
      res.setHeader("Access-Control-Allow-Origin", "*");
      res.send(resulttt);
    });
})

// app.use('/', indexRouter);
// app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
