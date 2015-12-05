<?php 
/**
*
* 2015/11/19
* 常炎隆
* porschegt23@foxmail.com
*
*/

header("Content-Type: text/html;charset=gbk");
//error_reporting(0);
$cookieVerify = dirname(__FILE__)."/zhihuVertify.tmp";
$cookieSuccess = dirname(__FILE__)."/zhihuSuccess.tmp";
define('USERNAME', ''); // 改为自己的学号
define('PASSWORD', ''); // 改为自己的密码
define('_Zhihu_URL', 'http://www.zhihu.com/');
session_start();

/**********
_xsrf:8f677ad0d6da9a563a0331e8b7a527e7
password:
captcha:fzyd
remember_me:true
email:
***********/
$headers_login = array("User-Agent" => "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36", 'Host'=>'www.zhihu.com', 'X-Requested-With'=> 'XMLHttpRequest', 'Referer'=> 'http://www.zhihu.com/', 'Connection' => 'keep-alive', 'Accept' => '*/*', 'Origin' => 'http://www.zhihu.com', 'Content-Type'=>'application/x-www-form-urlencoded; charset=UTF-8', 'Accept-Language'=>'zh-CN,zh;q=0.8,en;q=0.6', 'Cookie' => 'q_c1=8cb51eb51ed34c69bc44620bd6acb3cd|1449220944000|1449220944000; _za=29e19c3a-4c76-4d9a-b87f-94f7ea8f53ce; _xsrf=8f677ad0d6da9a563a0331e8b7a527e7; __utmt=1; cap_id="ZWJhYWIxY2NlM2Y3NDQzMzllZjAxYTBlZjQwNjNmYTI=|1449293651|e8ad670721467605d7d64a1d059be1a4dcd38ede"; __utma=51854390.1396146942.1449244880.1449246901.1449292993.3; __utmb=51854390.20.10.1449292993; __utmc=51854390; __utmz=51854390.1449292993.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|2=registration_date=20140919=1^3=entry_date=20151204=1; n_c=1'); 

if($_SESSION['go'] != 1){

	// 获取cookie并保存
	$ch = curl_init(); 
	curl_setopt($ch, CURLOPT_URL, _Zhihu_URL);
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 
	curl_setopt($ch, CURLOPT_COOKIEJAR, $cookieVerify);
	$rs = curl_exec($ch);
	curl_close($ch); 
 
	// 带上cookie抓取验证码，必须带上cookie，否则验证码不对应
	$ch = curl_init(); 
	curl_setopt($ch, CURLOPT_URL, _Zhihu_URL.'captcha.gif?r='.time());
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); 
	curl_setopt($ch, CURLOPT_COOKIEFILE, $cookieVerify);
	$rs = curl_exec($ch);
	// 把验证码在本地生成，二次拉取验证码可能无法通过验证
	@file_put_contents("zhihuVertify.jpg",$rs);
	curl_close($ch); 
	// 手工验证码表单
	echo "<form action=\"\" method=\"post\"><input type=\"text\" name=\"vcode\"><img src=\"zhihuVertify.jpg\" /><br><input type=\"submit\" value=\"ok\"></form>";
	$_SESSION['go'] = 1;
}else{
	// // 登录
	// $ch = curl_init(); 
	// $verify = $_POST["vcode"];
	// $url = _Zhihu_URL.'login/email'; 
 
	// // 返回结果存放在变量中，不输出 
	// curl_setopt($ch, CURLOPT_URL, $url);
	// curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
	// curl_setopt($ch, CURLOPT_HTTPHEADER, $headers_login); 
	// curl_setopt($ch, CURLOPT_COOKIEFILE, $cookieVerify);
	// curl_setopt($ch, CURLOPT_HEADER, 1); 
	// curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 120); 
	// curl_setopt($ch, CURLOPT_POST, true); 

	// /****
	// _xsrf:8f677ad0d6da9a563a0331e8b7a527e7
	// password:
	// captcha:fzyd
	// remember_me:true
	// email:
	// ****/
	// $fields_post = array("password"=> PASSWORD, "email"=> USERNAME, "remember_me"=>'true', "captcha" => $verify ,"_xsrf"=>"8f677ad0d6da9a563a0331e8b7a527e7"); 
	// $fields_string = ""; 
	// foreach($fields_post as $key => $value){ 
	// 	$fields_string .= $key . "=" . $value . "&"; 
	// } 

	// $fields_string = rtrim($fields_string , "&"); 
	// curl_setopt($ch, CURLOPT_HTTPHEADER, $headers_login); 
	// curl_setopt($ch, CURLOPT_COOKIEJAR, $cookieSuccess);
	// curl_setopt($ch, CURLOPT_POSTFIELDS, $fields_string);
	// curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
	// $result = curl_exec($ch);
	// printf_dump($result);
	// curl_close($ch);
	// // echo $fields_string;
	session_destroy();
	// // 登录成功,查看success.tmp cookie文件有相应用户名等信息

	// echo _Zhihu_URL.'captcha.gif?r='.intval(time()*1000);
}

function printf_dump($v){
	echo "<pre>";
	var_dump($v);
	echo "</pre>";
}
?> 