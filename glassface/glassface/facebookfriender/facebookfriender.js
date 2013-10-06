var page = require('webpage').create();

var loads = 0;
var system = require('system');
var email = system.args[1];
var pass = system.args[2];
var fbid = system.args[3];

page.onConsoleMessage = function(msg) {
    console.log(msg);
};

page.onLoadFinished = function() {
  loads++;
  if (loads == 2) {
      page.open("https://www.facebook.com/dialog/friends/?id="+fbid+"&app_id=154878534637314&redirect_uri=http://www.inspiratdesign.com/null.html", function(status){
        page.evaluate(function() {
          document.getElementById('u_0_0').click();
        });
      });
  };
};
 
page.open("https://www.facebook.com/", function(status) {
    if ( status === "success" ) {
        page.evaluate(function() {
              document.querySelector("input[name='email']").value = email;
              document.querySelector("input[name='pass']").value = pass;
              document.querySelector("#login_form").submit();
         });
   }
});
