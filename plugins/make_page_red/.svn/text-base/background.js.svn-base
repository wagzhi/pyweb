// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Called when the user clicks on the browser action.
chrome.browserAction.onClicked.addListener(function(tab) {
  var str='';
  
  win=chrome.extension.getViews()
  for (p in win){
  	str+=p+', ';
  }
 
  chrome.cookies.getAll({"name":"sbs_auth_uid",'url':'http://*.19lou.com/*'}, function(cookies){
	var cs=[];
	for (var i in cookies) {
      cs.push(cookies[i].name+"="+cookies[i].value+";\n");
    }
    alert(cs);
  });
});

chrome.browserAction.setIcon({path:"icon.png"});

chrome.extension.onRequest.addListener(
  function(request, sender, sendResponse) {
  	sender.tab? alert(sender.tab.url):alert("no tab");
    
    if (request.greeting == "hello")
      sendResponse({farewell: "goodbye"});
    else
      sendResponse({}); // snub them.
  });

/**
chrome.browserAction.setBadgeBackgroundColor({color:[0, 200, 0, 100]});

var i = 0;
window.setInterval(function() {
  chrome.browserAction.setBadgeText({text:String(i)});
  i++;
}, 10);
**/