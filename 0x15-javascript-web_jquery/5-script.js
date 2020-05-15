$('DIV#add_item').click(function () {
  $(this).nextAll('UL.my_list').append('<li>Item</li>');
});
