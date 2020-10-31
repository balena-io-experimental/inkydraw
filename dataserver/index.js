const CronJob = require("cron").CronJob;
const got = require("got");

const sampleData = [
  {
    x: 0,
    y: 0,
    w: 0.5,
    h: 0.2,
    type: "text",
    font_size: 16,
    content: "20:48 Plymouth",
  },
  {
    x: 0,
    y: 0.2,
    w: 0.5,
    h: 0.2,
    type: "text",
    content: "Departing now...",
  },
  {
    x: 0,
    y: 0.7,
    w: 1,
    h: 0.3,
    type: "text",
    align: "center",
    justify: "center",
    content: "20:54:33",
  },
];

const getContentLayout = async () => {
  return sampleData;
};

const poll = async () => {
  const contentLayout = await getContentLayout();

  try {
    await got.post("http://inkydraw:8080", {
      json: contentLayout,
      responseType: "json",
    });
  } catch (err) {
    console.error(err);
  }
};

const main = new CronJob("*/1 * * * *", poll, null, false, "Europe/Skopje");
main.start();
