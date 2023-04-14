<?php
	session_start();
	
	$request_method_check = $_SERVER["REQUEST_METHOD"];

	if(strtoupper($request_method_check) == 'GET'){
		
		$_p = '[';
		if($_SESSION['data']){
			foreach($_SESSION['data'] as $value){
				$_p .= '"'.$value.'",';
			}
			$_p = substr($_p, 0, -1);
		}
		
		$_p .= ']';
		
		if($_SESSION['data']){
			
			print_r($_p);

		}else{
			
			print_r($_p);
			
		}
		
	}else if(strtoupper($request_method_check) == 'POST'){
		
		if($_POST['body_msg']){
			$_SESSION['data'][] = $_POST['body_msg'];
			
			print_r(json_encode(["result" => true]));
			
		}else{
			
			print_r(json_encode(["result" => false]));
			
		}
		
	}else if(strtoupper($request_method_check) == 'DELETE'){
		
		$_SESSION['data'] = [];
		
		print_r(json_encode(["result" => true]));
		
	}

?>