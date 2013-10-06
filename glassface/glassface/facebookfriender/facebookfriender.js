var page = require('webpage').create();

var loads = 0;
var system = require('system');
var fbid = system.args[1];
var em = system.args[2];
var pas = system.args[3];

console.log('email', em);
console.log('pass', pas);
console.log('fbid', fbid);

page.onConsoleMessage = function(msg) {
    console.log(msg);
};

page.onLoadFinished = function() {
  loads++;
  console.log("load finished")
  if (loads == 2) {
      page.open("https://www.facebook.com/dialog/friends/?id="+fbid+"&app_id=154878534637314&redirect_uri=http://www.inspiratdesign.com/null.html", function(status){
        page.evaluate(function() {
          document.getElementById('u_0_0').click();
        });
      });
      page.render("debug.png");
      console.log("done");
      phantom.exit();
  };
};
 
page.open("https://www.facebook.com/", function(status) {
  console.log("opened", em);
    if ( status === "success" ) {
        page.evaluate(function(em, pas) {
              document.getElementById("email").value = em;
              document.getElementById("pass").value = pas;
              document.getElementById("login_form").submit();
         }, em, pas);
   }
});
