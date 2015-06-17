library(entropy)
library(jsonlite)

dirs = dir()[file.info(dir())$isdir]

for(dir in dirs){

    data = fromJSON(paste(dir, "/map.json", sep=""))

    data2 = fromJSON(paste(dir,"/response_curve.json", sep=""))

    T1 = table(data$next_step, data2$y)

    T1.mi <- mi.empirical(T1)

    ent = entropy(data$next_step)

    png(paste(dir,".png", sep=""))
    image(T1, xlab=paste(paste("MI: ",T1.mi), paste("Entropia: ", ent)))
    dev.off()
}

