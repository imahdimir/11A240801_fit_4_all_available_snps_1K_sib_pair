
list.of.packages <- c("data.table", "dplyr", "magrittr", "tidyverse", "plinkFile", "genio", "arrow")

lapply(list.of.packages, library, character.only = TRUE)


fn <- "/Users/mmir/Downloads/imputed_rs11586607.parquet"

df <- read_parquet(fn)


# Fit the OLS model
model <- lm(g1_plus_g2 ~ g1_minus_g2_hat, data = df)

# Summarize the model
summary(model)


model <- lm(g1_minus_g2 ~ g1_minus_g2_hat, data = df)

# Summarize the model
summary(model)
