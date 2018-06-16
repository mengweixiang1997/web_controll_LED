<?php

function msg($arg){

    $str = file_get_contents('config.txt');
    $str_encoding = mb_convert_encoding($str, 'UTF-8', 'UTF-8,GBK,GB2312,BIG5');
    $arr = explode("\n", $str_encoding);
    foreach ($arr as &$row){
        $row = trim($row);
    }	
    unset($row);
    $ip = str_replace("ip=","",$arr[0]);
    $port = str_replace("port=","",$arr[1]);



    $socket = socket_create(AF_INET,SOCK_STREAM,SOL_TCP);	
    if(socket_connect($socket, $ip, $port) == false){
        echo 'connect fail massege:'.socket_strerror(socket_last_error());
    }else{

        $message = $arg;
        $message = mb_convert_encoding($message,'GBK','UTF-8');

        if(socket_write($socket,$message,strlen($message)) == false){
            echo 'fail to write'.socket_strerror(socket_last_error());

        }else{
            while($callback = socket_read($socket,1024)){
		 $result  = PHP_EOL.$callback;
		 return $result;
            }
        }
    }
    socket_close($socket);
}


$result = "";
if(@$_GET["do"] != ""){
    header("Content-type:text/html;charset=utf-8");
    $result = msg($_GET['do']);
}



?>

<!DOCTYPE html>
<html>
<head lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<style type="text/css">

*{padding:0;margin:0;}
.opt, .btn{background-image:url("error");font-size:24px;line-height:1.8em;text-align:center;display:inline-block;border:none;background-color:#000;color:#fff;border:1px solid #fff;}
.info_servers{text-align:center;line-height:1.5em;width:100%;}
.module{width:480px;border:1px solid #000;}
.module .row{display:flex;width:100%;height:auto;}
.module .row .opt{width:50%;height:200px;}
.module .row .btn{width:20%;font-size:18px;line-height:4em}

@media (min-width:320px) and (max-width:480px){
.module{width:100%;height:auto;}


}

</style>
</head>
<body>



<div class="module">

    <h3 class="info_servers"> <?php echo($result); ?> </h3>

    <div class="row">
        <input type="button" value="on" onclick="javascript:send_msg('on')" class="opt">
        <input type="button" value="off" onclick="javascript:send_msg('off')" class="opt">
    </div>

    <div class="row">
        <input type="button" value="PIN_3" onclick="javascript:send_msg('light(3,0)')" class="btn">
        <input type="button" value="PIN_4" onclick="javascript:send_msg('light(4,0)')" class="btn">
        <input type="button" value="PIN_5" onclick="javascript:send_msg('light(5,0)')" class="btn">
        <input type="button" value="PIN_6" onclick="javascript:send_msg('light(6,0)')" class="btn">
        <input type="button" value="PIN_7" onclick="javascript:send_msg('light(7,0)')" class="btn">
    </div>
    

</div>




<script type="text/javascript">

function send_msg(arg){
    document.location.href= "?do=" + arg;
}


</script>


</body>
</html>
