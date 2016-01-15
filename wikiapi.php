<?php


print <<<_FORM_
<html>
<body>
<form action = "" method = "post">
<input type = "text" name = "name">
<input type = "submit" value = "送信">
</form>
_FORM_;
// キーワード指定
$keyword = $_POST["name"];

// APIのURL
$url = "http://wikipedia.simpleapi.net/api?keyword=".urlencode($keyword)."&output=php";

// データを取得
$data = file_get_contents($url) ;

// PHPシリアライズパーサーを利用して解析し、配列に入れる
$array = unserialize($data);

// 配列をforeachで表示するデモ
print "<H1>Wikipedia情報</H1>";
foreach ($array as $key => $value) {
    print "<a href=\"".$value[url]."\"><strong>".$value[title]."</strong></a>\n<br/>". $value[body] ."<hr/>\n\n";
}

print '(by <a href="http://www.simpleapi.net">SimpleAPI</a>:<a href="http://wikipedia.simpleapi.net">WikipediaAPI</a>)';
print "</body></html>";
?>
