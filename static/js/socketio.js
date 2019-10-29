function check_connection(socket){
  socekt.on('response', function(msg){
    console.log(msg.data)
  })
}
