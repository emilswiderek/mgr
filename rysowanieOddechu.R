data = read.csv("~/Pulpit/Uczelnia/Mgr/breath.txt")
library("ggplot2")
ggplot(data)+geom_line(aes(x=Time, y=HeartPhase))
