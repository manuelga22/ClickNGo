$("#signup").click(function() {
    $("#first").fadeOut("fast", function() {
    $("#second").fadeIn("fast");
    });
    });
    
    $("#signin").click(function() {
    $("#second").fadeOut("fast", function() {
    $("#first").fadeIn("fast");
    });
    });
    
    
      
             $(function() {
               $("form[name='login']").validate({
                 rules: {
                   
                   username: {
                     required: true,
                     username: true,

                   },
                   password: {
                     required: true,
                     
                   }
                 },
                  messages: {
                   username:{ 
                   username: "Please enter a username",
                  }
                   password: {
                     required: "Please enter password",
                    
                   }
                   
                 },
                 submitHandler: function(form) {
                   form.submit();
                 }
               });
             });
             $('#updateModal').on('shown.bs.modal', function () {
              $('#myInput').trigger('focus')
            })
            $('#deleteModal').on('shown.bs.modal', function () {
              $('#myInput').trigger('focus')
            })