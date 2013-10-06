var page = require('webpage').create();

var loads = 0;
var system = require('system');
var em = system.args[1];
var pas = system.args[2];

//console.log('email', em);
//console.log('pass', pas);

page.onConsoleMessage = function(msg) {
    console.log(msg);
};

page.onLoadFinished = function() {
  loads++;
  //console.log("load finished");
  console.log(loads);
  if (loads == 2) {
  // page.open("https://www.facebook.com/", function(status){
  //   console.log("ih");
  //   phantom.exit();
  //   console.log(page.);
  // });
   page.open("https://www.facebook.com/", function(status){
    var links = page.evaluate(function() {
        return [].map.call(document.querySelectorAll('li#navTimeline a'), function(link) {
            return link.getAttribute('href');
        });
    });
    console.log(links);
    console.log("test");
    phantom.exit();
  });
  }
};
 
page.open("https://www.facebook.com/", function(status) {
  //console.log("opened", em);
    if ( status === "success" ) {
        page.evaluate(function(em, pas) {
              document.getElementById("email").value = em;
              document.getElementById("pass").value = pas;
              document.getElementById("login_form").submit();
         }, em, pas);
   }
  //console.log("opened 2", em);
});
