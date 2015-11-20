<?php 
header("Content-Type: text/html;charset=utf-8");

/*
*
* 2015/11/19
* 常炎隆
* porschegt23@foxmail.com
*/
class loginSmarki
{
	private $username = '';
	private $md5pwd = '';
	private $cookie_file = '';

	function __construct($username,$md5pwd,$cookie_file)
	{
		$this->username = $username;
		$this->md5pwd = $md5pwd;
		$this->cookie_file = $cookie_file;
		$this->saveCookie();
		$this->loginWithCookie();
	}

	private function saveCookie(){
		$ch = curl_init("http://smartki.sinaapp.com/action/User.php?action=login");
		curl_setopt($ch, CURLOPT_HEADER, 0);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_POST, 1);
		curl_setopt($ch, CURLOPT_POSTFIELDS, "username=$this->username&password=$this->md5pwd&is_ajax=1");
		curl_setopt($ch, CURLOPT_COOKIEJAR, $this->cookie_file);
		curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
		$arr = curl_exec($ch);
		curl_close($ch);
	}

	private function loginWithCookie(){
		$url = "http://smartki.sinaapp.com";
		$ch = curl_init($url);
		curl_setopt($ch, CURLOPT_HEADER, 0);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_COOKIEFILE, $this->cookie_file);
		curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
		$contents = curl_exec($ch);
		$this->printf_dump($contents);
		curl_close($ch);
	}

	private function printf_dump($v){
		echo "<pre>";
		var_dump($v);
		echo "</pre>";
	}
}
/***
http://jwxt.sxau.edu.cn/loginAction.do
zjh1=&tips=&lx=&evalue=&eflag=&fs=&dzslh=&zjh=20131111111&mm=111111&v_yzm=9yr9
***/

/******** 用户名、密码 *********/
$username = 'test';
$password = md5($username);
/******** cookie目录  *********/
$cookie_file = dirname(__FILE__).'/cookie.txt';

$Smarki = new loginSmarki($username,$password,$cookie_file);
?> 