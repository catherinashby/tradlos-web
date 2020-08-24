//
document.addEventListener("DOMContentLoaded", function(){
  // Handler when the DOM is fully loaded
  if ( document.documentMode || document.attachEvent )    {
    document.querySelector( 'html' ).classList.add( 'ie' );
  }

  document.querySelector('#user_menu').addEventListener("click", function(){
    this.parentElement.querySelector('ul').classList.toggle('hidden');
    return;
  })
});
