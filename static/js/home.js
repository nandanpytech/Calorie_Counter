function openNav() {
    document.getElementById("myNav").style.width = "88%";
  }
  
  function closeNav() {
    document.getElementById("myNav").style.width = "0%";
  }

  function arrow(){
    document.getElementById('grid').style.width="35%"
    document.getElementById('wrong').style.width="20%";
    document.getElementById('arrow').style.width= "0%"
  }
  function wrong(){
    document.getElementById('grid').style.width="0%"
    document.getElementById('wrong').style.width="0%";
    document.getElementById('arrow').style.width= "20%"
  }

$('.slider').slick({
  dots: true,
  infinite: false,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 4,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});