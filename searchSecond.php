<?php 
header("Content-Type: text/html;charset=gbk");
//error_reporting(0);
$cookieVerify = dirname(__FILE__)."/verify.tmp";
$cookieSuccess = dirname(__FILE__)."/success.tmp";
define('USERNAME', '20131613115'); // 改为自己的学号
define('PASSWORD', '881520'); // 改为自己的密码
session_start();
if($_SESSION['go'] != 1){
	echo "<script>alert('password right~');</script>";
	// 获取cookie并保存
	$ch = curl_init(); 
	curl_setopt($ch, CURLOPT_URL, "http://jwxt.sxau.edu.cn/loginAction.do");
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 
	curl_setopt($ch, CURLOPT_COOKIEJAR, $cookieVerify);
	$rs = curl_exec($ch);
	curl_close($ch); 
 
	// 带上cookie抓取验证码，必须带上cookie，否则验证码不对应
	$ch = curl_init(); 
	curl_setopt($ch, CURLOPT_URL, "http://jwxt.sxau.edu.cn/validateCodeAction.do?random=0.9432079987600446");
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 
	curl_setopt($ch, CURLOPT_COOKIEFILE, $cookieVerify);
	$rs = curl_exec($ch);
	// 把验证码在本地生成，二次拉取验证码可能无法通过验证
	@file_put_contents("verify.jpg",$rs);
	curl_close($ch); 
	// 手工验证码表单
	echo "<form action=\"\" method=\"post\"><input type=\"text\" name=\"vcode\"><img src=\"verify.jpg\" /><br><input type=\"submit\" value=\"ok\"></form>";
	$_SESSION['go'] = 1;
}else{
	// 登录
	$ch = curl_init(); 
	$verify = $_POST["vcode"];
	$url = "http://jwxt.sxau.edu.cn/loginAction.do"; 
 
	// 返回结果存放在变量中，不输出 
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	curl_setopt($ch, CURLOPT_COOKIEFILE, $cookieVerify);
	curl_setopt($ch, CURLOPT_HEADER, 1); 
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 120); 
	curl_setopt($ch, CURLOPT_POST, true); 

	//zjh1=&tips=&lx=&evalue=&eflag=&fs=&dzslh=&zjh=20131613115&mm=881520&v_yzm=9yr9
	$fields_post = array("zjh"=> USERNAME, "mm"=> PASSWORD, "v_yzm"=>$verify); 
	$headers_login = array("User-Agent" => "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"); 
	$fields_string = ""; 
	foreach($fields_post as $key => $value){ 
		$fields_string .= $key . "=" . $value . "&"; 
	} 

	$fields_string = rtrim($fields_string , "&"); 
	curl_setopt($ch, CURLOPT_HTTPHEADER, $headers_login); 
	curl_setopt($ch, CURLOPT_COOKIEJAR, $cookieSuccess);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $fields_string);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
	$result = curl_exec($ch);
	dump($result);
	curl_close($ch);
	echo $fields_string;
	session_destroy();
	// 登录成功,查看success.tmp cookie文件有相应用户名等信息
}

function dump($v){
	echo "<pre>";
	var_dump($v);
	echo "</pre>";
}
?> 