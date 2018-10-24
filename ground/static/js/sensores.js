
$(document).ready(function() {
    var g1 = new JustGage({
        id: 'gauge1',
        value: 0,
        min: 0,
        max: 100,
        title: "Umidade do solo (%)",
        levelColorsGradient: true
    
    });
    var g2 = new JustGage({
        id: 'gauge2',
        value: 0,
        min: 0,
        max: 100,
        title: "Umidade do solo (%)",
        levelColorsGradient: true
        
    });
    var g3 = new JustGage({
        id: 'gauge3',
        value: 0,
        min: 0,
        max: 100,
        title: "Umidade do solo (%)",
        levelColorsGradient: true
        
    });
    var g4 = new JustGage({
        id: 'gauge4',
        value: 0,
        min: 0,
        max: 100,
        title: "Umidade do solo (%)",
        levelColorsGradient: true
        
    });
    
    //UM BOTAO PARA CADA SENSOR
    $('#medir-button1').click(function(){       
        let medicao1  = setInterval(function(){
         $.ajax({
             type:"POST",
             url: '/medicao',
             data: {
                    'sensor': 0
                    },   
             success: function(resposta){
                g1.refresh(resposta);
                                                   
             }
        });
        $('#stop-button1').click(function(){
            clearInterval(medicao1);
    
        });

        }, 1000);
    })

    //UM BOTAO PARA CADA SENSOR
    $('#medir-button2').click(function(){       
        let medicao1  = setInterval(function(){
         $.ajax({
             type:"POST",
             url: '/medicao',
            data: {
                    'sensor': 1
                    },   
             success: function(resposta){
                g2.refresh(resposta);
                                                   
             }
        });
        $('#stop-button2').click(function(){
            clearInterval(medicao1);
    
        });

        }, 2000);
    })

    //UM BOTAO PARA CADA SENSOR
    $('#medir-button3').click(function(){       
        let medicao1  = setInterval(function(){
         $.ajax({
             type:"POST",
             url: '/medicao',
             data: {
                    'sensor': 2
                    },    
             success: function(resposta){
                g3.refresh(resposta);
                                                   
             }
        });
        $('#stop-button3').click(function(){
            clearInterval(medicao1);
    
        });

        }, 3000);
    })


    //UM BOTAO PARA CADA SENSOR
    $('#medir-button4').click(function(){       
        let medicao1  = setInterval(function(){
         $.ajax({
             type:"POST",
             url: '/medicao',
             data: {
                    'sensor': 3
                    }, 
             success: function(resposta){
                g4.refresh(resposta);
                                                   
             }
        });
        $('#stop-button4').click(function(){
            clearInterval(medicao1);
    
        });

        }, 4000);
    })
 
    //CALIBRAR DE CADA SENSOR
    $('#calibrar-button1').click(function(){
        console.log('calibrando1..')
        
        minutes = 600; //em segundos
        count= minutes;
        soma = 0 ;
        final = 0;
        sensor = 0;

        var calibrar = setInterval(function(){
        if (count < 0){
            clearInterval(calibrar);
            $.ajax({
                type:"POST",
                url:'/calcula_peso',
                data: {
                        'divisor' : minutes,
                        'sensor': sensor
                        },
                success: function(resposta){
                    console.log(resposta);
                    if(resposta == "sucesso"){
                        $('.medicaosensor1').show();
                        $('#calibrando1').hide();
                        $('.ok_calib_1').show();
                        $('.error_calib_1').hide();
                        
                        console.log('peso ajustado');
                    }
                    
                }
            });
                            
        }else{
            
            $.ajax({
                type:"POST",
                url:'/calibrar',
                data: {
                        'start' : soma,
                        'sensor': sensor
                        },
                success: function(resposta){
                    soma = soma + parseInt(resposta);
                    count= count - 1;
                    console.log('sensor: '+sensor );
                    final = parseFloat(resposta).toFixed(4);
                    $('.peso_sensor_0').text(final);

                }
            });
        }

        },1000);

    })

    $('#calibrar-button2').click(function(){
        console.log('calibrando2..')

    })

    $('#calibrar-button3').click(function(){
        console.log('calibrando3..')

    })

    $('#calibrar-button4').click(function(){
        console.log('calibrando4..')

    })

    $('.calibrar-button').click(function(){
        box = $(this).parent().parent().parent();
        calibrando = box.find(".box-calibrando");
        medindo = box.find(".box-medindo");
        calibrando.show();
        medindo.hide();

    });

    $('.play-button').click(function(){
        stop = $(this).parent().find(".stop-button")
        $(this).hide();
        stop.show();
    });
    
    $('.stop-button').click(function(){
        play = $(this).parent().find(".play-button")
        $(this).hide();
        play.show();
    });

    

});