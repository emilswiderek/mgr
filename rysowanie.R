data = read.csv("~/Pulpit/Uczelnia/Mgr/HeartPhase.txt")
library("ggplot2")
data$Breathing = data$Breath
data$BreathingShape = data$Breath
sapply(1:length(data$Time), function(x){
if(data$Breath[x] == 1){
	data$Breathing[x] <<- "red"
	data$BreathingShape <<- 10
} else {
	data$Breathing[x] <<- "Blue"
	data$BreathingShape <<- 1
}
});
ggplot(data)+geom_point(aes(x=Time, y=HeartPhase, fill=data$Breath))
