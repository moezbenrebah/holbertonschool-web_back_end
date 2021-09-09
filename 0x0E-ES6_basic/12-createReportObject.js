export default function createReportObject(employeesList) {
  const allEmployees = {};
  for (const [k, v] of Object.entries(employeesList)) {
    allEmployees[`${k}`] = v;
  };

  return { allEmployees, getNumberOfDepartments: (employeesList) => Object.keys(employeesList).length };
};
