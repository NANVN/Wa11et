let blocks = document.getElementsByTagName("td");
for(let i=0;i<blocks.length;i++){
    if((i+2)%7==0||(i+1)%7==0)
    {blocks[i].style.background = "#7bbd9d";
	    blocks[i].style.color = "red";}
    else
    {blocks[i].style.background = "linear-gradient(45deg, #5899E2, #FFFFFF)";}}
