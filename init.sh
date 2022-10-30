# create simple commmand line interface
# in: $1 - command
#     $2 - parameter
# list: ["start", "stop", "restart", "status"]
# list out: ["Starting", "Stopping", "Restarting", "Ok"]

# echo table of current commands and description when no args
if [ $# -eq 0 ]; then
	echo "Usage: $0 [command] [parameter]"
	echo "Commands:"
	echo "  start [name] - start service"
	echo "  stop [name] - stop service"
	echo "  restart [name] - restart service"
	echo "  status [name] - status service"
	exit 0
fi

case $1 in
	"start")
		echo "Starting $2"
		;;
	"stop")
		echo "Stopping $2"
		;;
	"restart")
		echo "Restarting $2"
		;;
	"status")
		echo "Ok"
		;;
	*)
		echo "Unknown command"
		;;
esac