<?php
/**
setLang=us&ext=mp3&

voiceSelector=48&

text=Hello.&

send=Play&

csrfield=CLAzzoc8I4X6HTu6M2Sj2BoHXInTQj3D&

ref-form-name=VoiceTesterForm;
**/
session_start();
function dump($v){
	echo "<pre>";
	var_dump($v);
	echo "</pre>";
}

$requestURL = 'https://www.ivona.com/let-it-speak/?setLang=us';
$requestText = 'hello.';
$requestStr = 'setLang=us&ext=mp3&voiceSelector=48&text=Hi+there%2C+your+name+is+Salli.+I+am+one+of+the+IVONA+voices.+I+will+read+anything+you+want.+Enter+any+text+here+and+click+Play.&send=Play&csrfield=CLAzzoc8I4X6HTu6M2Sj2BoHXInTQj3D&ref-form-name=VoiceTesterForm';

$ch = curl_init(); 
// 返回结果存放在变量中，不输出 
curl_setopt($ch, CURLOPT_URL, $requestURL);
// curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
// curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 120); 
curl_setopt($ch, CURLOPT_POST, true); 
curl_setopt($ch, CURLOPT_POSTFIELDS, $requestStr);

$result = curl_exec($ch);
dump($result);
curl_close($ch);
?>
