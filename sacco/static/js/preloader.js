/**
 * Created by polyc on 25/11/2016.
 */
// Complete page is fully loaded, including all frames, objects and images
$(window).load(function() {
  // Remove preloader
  // https://ihatetomatoes.net/create-custom-preloading-screen/
  $('body').addClass('loaded');
});