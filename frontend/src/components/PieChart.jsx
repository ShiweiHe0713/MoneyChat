import Tablue from Tablaue;

async function PieChart() {
    // Month should be retrieved from UI
    const month = 3;
    const response = await fetch("http://127.0.0.1:5000/pieChart", {
        method: 'POST',
        body: {
            month: `${month}`
        },
    });

    if(!response.ok) {
        console.error('Error recieving response from server')
    } else {
        // Show the pie chart on the client
        // Use tablaue or oather BI platform to visual the 
        const tablaue_object = New Tablue();
        tablaue_object.data = response.data;
        tablaue_object.Xaxis = category;
        tablaue_object.yaxis = expense;
        tablaue_plot = new tablaue_object.plot();
        tableu_plot.plot(tablaue_object);
        return tablaue_plot;
    }
}

export default PieChart;