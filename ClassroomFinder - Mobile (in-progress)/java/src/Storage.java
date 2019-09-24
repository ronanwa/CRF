import java.util.ArrayList;

public class Storage {
        ArrayList<CourseInfo> storage;

        public Storage(){
                storage = new ArrayList<CourseInfo>();
        }

//        public ArrayList<CourseInfo> getStorage(){
//                return storage;
//        }

        public void addCourse(CourseInfo course){
                storage.add(course);
        }
        public void removeCourse(CourseInfo course){
                storage.remove(course);
        }
       public CourseInfo get(CourseInfo course){
               return storage.get(storage.indexOf(course));
       }
}
