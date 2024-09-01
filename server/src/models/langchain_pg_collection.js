'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class langchain_pg_collection extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  langchain_pg_collection.init({
    id: DataTypes.UUID,
    name: DataTypes.STRING,
    merchantId: DataTypes.INTEGER
  }, {
    sequelize,
    modelName: 'langchain_pg_collection',
  });
  return langchain_pg_collection;
};