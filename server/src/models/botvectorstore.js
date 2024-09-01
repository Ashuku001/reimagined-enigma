'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class BotVectorStore extends Model {
    static associate(models) {
      this.belongsTo(models.Merchant, {foreignKey: "merchantId", as: "botVectors"})
    }
  }
  BotVectorStore.init({
    original: DataTypes.TEXT,
    vector: DataTypes.BLOB,
    merchantId: DataTypes.INTEGER,
  }, {
    sequelize,
    modelName: 'BotVectorStore',
  });
  return BotVectorStore;
};