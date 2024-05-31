// Transaction class 
// Date,Description,Amount,Running Bal.,
const { Model, DataTypes } = require('sequelize');
const transaction_db = require('')

class Transaction extends Model {};

Transaction.init(
    {
        ID: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true,
        },
        Date: {
            type: DataTypes.DATE,
            allowNull: false,
        },
        Amount: {
            type: DataTypes.FLOAT,
            allowNull: false,
        },
        Balance: {
            type: DataTypes.FLOAT,
            allowNull: false,
        },
        Description: {
            type: DataTypes.STRING,
            allowNull: true,
        },
    },
    {
        transaction_db,
        modelName: "Transaction_DB",
        timestamps: false,
        tableName: "Transactions",
    }
)
