
$("#id_email").change(function () {
  var form = $("#login-form");
  $.ajax({
    url: form.attr("data-validate-email-url"),
    data: form.serialize(),
    dataType: 'json',
    success: function (data) {
    console.log(data);
      if (data.is_taken) {
        alert(data.error_message);
      }
     // /*
      else{
		 alert(data.error_message);
      }
     // */
    }
  });

});

