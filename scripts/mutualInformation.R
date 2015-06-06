library(entropy)
library(jsonlite)

data = fromJSON("../0.408805031_sinus_map.json")

data2 = fromJSON("../0.408805031_sinus_response.json")

T1 = table(data$next_step, data2$y)

T1.mi <- mi.empirical(T1)
image(T1)

