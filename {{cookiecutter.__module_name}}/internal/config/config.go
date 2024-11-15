package config

import (
	"os"

	"gopkg.in/yaml.v3"
)

type Config struct {
	// AppName is the name of the application.
	AppName string `yaml:"app_name"`
	// AppVersion is the version of the application.
	AppVersion string `yaml:"app_version"`
}

func LoadConfig(path string) (cfg *Config, err error) {
	cfg = &Config{}

	if path == "" {
		cfg.AppName = "MyApp"
		cfg.AppVersion = "1.0.0"
		return
	}

	data, err := os.ReadFile(path)
	if err != nil {
		return
	}

	err = yaml.Unmarshal([]byte(data), cfg)
	if err != nil {
		return
	}

	return
}
