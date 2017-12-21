
                $("#click-me0").click(function () {
                    $.ajax({
                        success: function (data) {                               
                            console.log(data);   
                            $('#info-modal0').addClass("show"); 
                        },
                        async: true
                    });
                });
                $(".modal-dialog0 .close").click(function(){
                    $(this).closest(".modal-dialog0").removeClass("show");
                });
                
                $("#click-me1").click(function () {
                    $.ajax({
                        success: function (data) {                               
                            console.log(data);   
                            $('#info-modal1').addClass("show"); 
                        },
                        async: true
                    });
                });
                $(".modal-dialog1 .close").click(function(){
                    $(this).closest(".modal-dialog1").removeClass("show");
                });
                
                $("#click-me2").click(function () {
                    $.ajax({
                        success: function (data) {                               
                            console.log(data);   
                            $('#info-modal2').addClass("show"); 
                        },
                        async: true
                    });
                });
                $(".modal-dialog2 .close").click(function(){
                    $(this).closest(".modal-dialog2").removeClass("show");
                });
                
                $("#click-me3").click(function () {
                    $.ajax({
                        success: function (data) {                               
                            console.log(data);   
                            $('#info-modal3').addClass("show"); 
                        },
                        async: true
                    });
                });
                $(".modal-dialog3 .close").click(function(){
                    $(this).closest(".modal-dialog3").removeClass("show");
                });
                
                $("#click-me4").click(function () {
                    $.ajax({
                        success: function (data) {                               
                            console.log(data);   
                            $('#info-modal4').addClass("show"); 
                        },
                        async: true
                    });
                });
                $(".modal-dialog4 .close").click(function(){
                    $(this).closest(".modal-dialog4").removeClass("show");
                });
                
                var baseUrl = "http://api.wordnik.com/v4/word.json/";
    			var apiKey = "44292d2d0bb36bdb80001084ac6037c2947d0b87460c1fb95";
    			function getSynonyms (theWord, callback) {
    				var url = baseUrl + theWord + "/relatedWords?useCanonical=true&relationshipTypes=synonym&limitPerRelationshipType=100&api_key=" + apiKey;
    				var jxhr = $.ajax ({ 
    					url: url,
    					dataType: "text" , 
    					timeout: 30000 
    					}) 
    				.success (function (data, status) { 
    					var array = JSON.parse (data);
    					console.log (data);
    					callback (array [0].words)
    					}) 
    				.error (function (status) { 
    					console.log ("getSynonyms: url == " + url + ", error == " + JSON.stringify (status, undefined, 4));
    					});
    				}
    		