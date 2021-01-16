function step(container, data)
{
    var layout = {
                title: {
                    text:"Step Response"
                    },
                xaxis: {
                    title: {
                        text: 'time [s]'
                        }
                    },
                yaxis: {
                    title: {
                        text: 'output'
                        }
                    }
                };
    Plotly.newPlot(container, [{x:data["t"],y:data["s"]}],layout);
}

function bode(container, data)
{
    var layout = {
                grid: {
                    rows: 2,
                    columns: 1,
                    subplots:['xy','xy2'],
                },
                title: {
                    text:"Bode Diagram"
                    },
                xaxis: {
                    type: 'log',
                    autorange: true,
                    title: {
                        text: 'Angular Frequency [rad/s]'
                        }
                    },
                yaxis: {
                    type: 'log',
                    autorange: true,
                    title: {
                        text: 'Magnitude'
                        }
                    },
                yaxis2: {
                    title: {
                        text: 'Phase [deg]'
                        }
                    }
    };

    var trace1 = {
        x: data["w"],
        y: data["abs"],
        type: 'scatter'
    };

    var trace2 = {
        x: data["w"],
        y: data["phase"],
        type: 'scatter',
        xaxis: 'x',
        yaxis: 'y2'
    };

    console.log([trace1,trace2])
    Plotly.newPlot(container, [trace1,trace2],layout);
}

function zpk(container, data)
{
    var layout = {
                title: {
                    text:"ZP map"
                    },
                xaxis: {
                    title: {
                        text: 'Real Part'
                        }
                    },
                yaxis: {
                    scaleanchor: 'x',
                    title: {
                        text: 'Imag Part'
                        }
                    }
                };

    var trace1 = {
        x: data["poles"]["real"],
        y: data["poles"]["imag"],
        type: 'scatter',
        mode: 'markers',
        marker: { size: 12, symbol: 'x' }
    };

    var trace2 = {
        x: data["poles"]["real"],
        y: data["zeros"]["imag"],
        type: 'scatter',
        mode: 'markers',
        marker: { size: 12, symbol: 'o'}
    };

    Plotly.newPlot(container, [trace1,trace2],layout);
}
