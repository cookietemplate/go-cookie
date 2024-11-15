package utils

import (
	"fmt"
	"time"
)

func FormatInfos(appName string, appVersion string, text string) string {
	return fmt.Sprintf("%s - %s[%s]: %s", time.Now().Format("2006-01-02 15:04:05"), appName, appVersion, text)
}
