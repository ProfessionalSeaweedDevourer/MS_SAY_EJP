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


// -------------  기존 코드  ----------------
// app.use('/', indexRouter);
// app.use('/users', usersRouter);
// -----------    테스트 코드    ----------------
app.listen(9999); // node.js express WAS 포트번호
// app.post();
app.get("/te.st", function (reqqq, resss) {
  resss.send("abcd");
});

app.get("/html.test", function (req, res) {
  html = "<html><head><meta charset=\"utf-8\"></head><body>"
  html += "<marquee> test </marquee>"
  html += "</body></html>"
  res.send(html)
});

// parameter 테스트
app.get("/param.test", function (req, res) {
  var aa = req.query.a;
  var bb = req.query.b;
  var cc = aa + bb; // '수'로 형변환하지 않았기 때문에 둘을 이어붙인 값이 나옴
  var html = "<html><head><meta charset=\"utf-8\"></head><body>"
  html += "<h1>" + cc + "</h1>";
  html += "</body></html>"
  res.send(html)
});

// 신세대 web: xml/json을 만들어서 응답을 주고받고 front-end에서 처리
app.get("/json.test", function (req, res) {
  var aa = req.query.a * 1;
  var bb = req.query.b * 1;
  var cc = aa + bb;
  var dd = {"result": cc};
  res.setHeader("Access-Control-Allow-Origin", "*")
  res.send(dd);
});

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
