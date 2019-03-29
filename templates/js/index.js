skrollr.init()

$(".logocon").click(function(){
  $("html, body").animate({ scrollTop: 100 });
});

/* HEY THERE!
I use Internet Explorer 11. I like it for its speed, but its standards support lacks in some areas: I like to say "Make it work in IE, you're probably done."

Well, not this time, Ovi! In webkit/blink the whole thing gets nudged down 20vh declared in the .content class using margin-top...

I used "top" on the content div in place of "margin-top", now works the same way in IE as before, whereas in webkit/blink this fixes the issue. If you use FF, you can tell me in the comments if anything appears broken.
*/