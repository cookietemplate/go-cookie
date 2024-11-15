package main

import (
	"{{cookiecutter.project_slug}}/internal/config"
	"{{cookiecutter.project_slug}}/internal/utils"
	"{{cookiecutter.project_slug}}/pkg/hello"
	"flag"

	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
)

func main() {
	configPath := flag.String("path", "", "Configuration file path")
	flag.Parse()

	cfg, err := config.LoadConfig(*configPath)
	if err != nil {
		panic(err)
	}

	zerolog.TimeFieldFormat = zerolog.TimeFormatUnix

	helloText := hello.SayHello(cfg.AppName)
	log.Info().
		Str("Hello String", utils.FormatInfos(cfg.AppName, cfg.AppVersion, helloText)).
		Int("Number of characters", len(helloText)).
		Msg("Hello message")
}
