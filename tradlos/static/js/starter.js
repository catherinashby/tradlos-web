//
document.addEventListener("DOMContentLoaded", function(){
  // Handler when the DOM is fully loaded
  if ( document.documentMode || document.attachEvent )    {
    document.querySelector( 'html' ).classList.add( 'ie' );
  }
  var btn = document.querySelector('#user_menu');
  if ( btn ) {
    btn.addEventListener("click", function(){
      this.parentElement.querySelector('ul').classList.toggle('hidden');
      return;
    })
  }
});
