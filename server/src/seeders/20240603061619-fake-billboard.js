"use strict";

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.bulkInsert(
      "Billboards",
      [
        {
          label: "My Fake Store",
          storeId: 10,
          id: 20,
          imageUrl: "https://res.cloudinary.com/dzeeuz5g6/image/upload/v1702201840/qa9iszb4ebczgxffka5n.jpg",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
      ],
      {}
    );
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     */
    await queryInterface.bulkDelete("Billboards", null, {});
  },
};
