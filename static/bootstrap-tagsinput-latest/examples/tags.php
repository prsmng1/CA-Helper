<!DOCTYPE html>
<html>
  <head>
    <title>Bootstrap Tags Input</title>
    <meta name="robots" content="index, follow" />
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/css/bootstrap.min.css">
    
    <link rel="stylesheet" href="../dist/bootstrap-tagsinput.css">
    
  </head>
  <body>
   
    <div class="container">
      <section id="examples">
       <div class="bs-example">
		<form name="myForm" action="send.php" method="POST" enctype="multipart/form-data">	
					<input type="file" name="file[]" multiple >
					<input type="text" name="tag" placeholder="gst2020 , tax2019"  value="" data-role="tagsinput">
					<input type="submit" name="submit" value="upload">
				</form>
		

          </div>

       
      </section>
    </div>
    

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <script src="../dist/bootstrap-tagsinput.min.js"></script>
     
	
	
  </body>
</html>

